"use client";
import Image from "next/image";
import styles from "./classification.module.css";
import { useRef, useState } from "react";
import { Predict } from "@/app/http/predict-request";
interface ClassificationProps {
  file?: File;
  model: string | null;
  fruit: string | null;
}

interface PredictionResponse {
  prediction: string;
  label: string;
  quality: string;
}

export default function Classification({
  file,
  model,
  fruit,
}: ClassificationProps) {
  let fileSrc = "";
  if (file !== undefined) {
    fileSrc = URL.createObjectURL(file);
  }
  const [result, setResult] = useState<PredictionResponse>({
    prediction: "",
    label: "",
    quality: "",
  });
  const resultQualityRef = useRef<any>(null);
  const handleClassification = async () => {
    console.log(resultQualityRef);
    if (resultQualityRef != null) {
      resultQualityRef.current.textContent = "Aguardando resultado...";
    }

    const res = await Predict(model!, fruit!, file!);
    if (res) {
      setResult(res);
      resultQualityRef.current.textContent = res.quality;
    }
  };

  return (
    <article className={styles.container}>
      <section className={styles.imageContainer}>
        <h1>Imagem Selecionada</h1>
        {fileSrc == "" ? (
          <div className={styles.imageMock}></div>
        ) : (
          <Image src={fileSrc} alt="uploaded image" height={300} width={300} />
        )}
        <button
          onClick={handleClassification}
          className={styles.classifyButton}
          style={{ display: fileSrc == "" ? "none" : "block" }}
        >
          Classificar
        </button>
      </section>
      <section className={styles.resultContainer}>
        <h1>Resultados</h1>
        <div>
          <ul className={styles.results}>
            {result && (
              <li
                className={`${styles.health} ${+result.label == 0 ? styles.healthy : styles.unhealthy
                  }`}
                ref={resultQualityRef}
              >
              </li>
            )}
          </ul>
        </div>
      </section>
    </article>
  );
}

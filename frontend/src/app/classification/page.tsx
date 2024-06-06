"use client";
import Card from "../_components/card/card";
import styles from "./page.module.css";

import { ArrowRight } from "react-feather";
import { useSearchParams } from "next/navigation";
import SideBar from "../_components/sidebar/sidebar";
import Image from "next/image";
import { useState } from "react";
import Classification from "../_components/classification/classification";

export default function Page() {
  const searchParams = useSearchParams();
  const model = searchParams.get("model");
  const fruit = searchParams.get("fruit");
  const [uploadedImage, setUploadedImage] = useState<File>();
  const fruits = ["Morango", "Pêssego", "Romã"];
  const models = ["ResNet", "EfficientNet"];

  const handleFileUpload = (file: File) => {
    setUploadedImage(file);
  };

  return (
    <section className={styles.container}>
      <h1 className={styles.pageTitle}>Classificação</h1>
      <div className={styles.wrapper}>
        <section className={styles.classificationSideBar}>
          <SideBar
            title="Classificar Fruta"
            fruits={fruits}
            models={models}
            onFileSelected={handleFileUpload}
          />
        </section>
        <section className={styles.classificationContainer}>
          <Classification file={uploadedImage} model={model} fruit={fruit} />
        </section>
      </div>
    </section>
  );
}

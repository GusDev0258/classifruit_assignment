"use client";
import { usePathname, useSearchParams, useRouter } from "next/navigation";
import styles from "./sidebar.module.css";
import {
  ChangeEvent,
  ElementType,
  useCallback,
  useEffect,
  useRef,
  useState,
} from "react";
import { UploadCloud } from "react-feather";

interface SideBarProps {
  title: string;
  models: string[];
  fruits: string[];
  onFileSelected: (file: File) => void;
}

export default function SideBar({
  title,
  models,
  fruits,
  onFileSelected,
}: SideBarProps) {
  const searchParams = useSearchParams();
  const [activeModel, setActiveModel] = useState(searchParams.get("model"));
  const [activeFruit, setActiveFruit] = useState(searchParams.get("fruit"));
  const pathname = usePathname();
  const { replace } = useRouter();

  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const params = new URLSearchParams();
    if (activeModel) params.set("model", activeModel);
    if (activeFruit) params.set("fruit", activeFruit);
    replace(`${pathname}?${params.toString()}`);
  }, [activeModel, activeFruit, pathname]);

  const handleModelClick = (model: string) => {
    setActiveModel(model.toLowerCase());
  };

  const handleFruitClick = (fruit: string) => {
    setActiveFruit(
      fruit
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase()
    );
  };

  const handleUploadClick = () => {
    fileInputRef.current!.click();
  };

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const files: FileList = event.target.files!;
    const file: File = files[0];
    onFileSelected(file);
  };

  return (
    <aside className={styles.container}>
      <div className={styles.titleContainer}>
        <h1 className={styles.sideBarTitle}>{title}</h1>
      </div>
      <section className={styles.modelsContainer}>
        <h1 className={styles.sideBarTitle}>Modelos</h1>
        {models.map((model, index) => (
          <div key={index}>
            <button
              className={`${styles.optionButton} ${
                model.toLocaleLowerCase() === activeModel ? styles.active : ""
              }`}
              onClick={() => handleModelClick(model)}
            >
              {model}
            </button>
          </div>
        ))}
      </section>
      <section className={styles.fruitsContainer}>
        <h1 className={styles.sideBarTitle}>Frutas</h1>
        {fruits.map((fruit, index) => (
          <div key={index}>
            <button
              className={`${styles.optionButton} ${
                fruit
                  .toLocaleLowerCase()
                  .normalize("NFD")
                  .replace(/[\u0300-\u036f]/g, "") === activeFruit
                  ? styles.active
                  : ""
              }`}
              onClick={() => handleFruitClick(fruit)}
            >
              {fruit}
            </button>
          </div>
        ))}
      </section>
      <section className={styles.uploadContainer}>
        <button className={styles.uploadButton} onClick={handleUploadClick}>
          <UploadCloud />
          Subir Imagem
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileChange}
            style={{ display: "none" }} // Hide the file input
            multiple={false}
            accept="image/jpg, image/jpeg"
          />
        </button>
      </section>
    </aside>
  );
}

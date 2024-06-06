import Image from "next/image";
import styles from "./page.module.css";
import Button from "./_components/button/button";
import { ArrowRight } from "react-feather";
export default function Home() {
  return (
    <main className={styles.container}>
      <h1 className={styles.landingTitle}>
        Classifique Frutas
        <div className={styles.spanContainer}>
          <span className={styles.healthy}>Saudáveis</span>
          ou
          <span className={styles.rotten}>Podres</span>
        </div>
      </h1>
      <Button text={"Iniciar"} icon={ArrowRight} href={"/model"} />
    </main>
  );
}

import Card from "../_components/card/card";
import styles from "./page.module.css";
import { Codesandbox } from "react-feather";
export default function Page() {
  return (
    <section className={styles.container}>
      <h1 className={styles.pageTitle}>Escolha o modelo</h1>
      <section className={styles.cardContainer}>
        <Card
          btnHref={"/fruits/?model=resnet"}
          btnIcon={Codesandbox}
          cardName="ResNet"
          imgSrc={"/images/resnet.jpg"}
          nameBg="#cbd5e1"
          nameColor="#334155"
        />
        <Card
          btnHref={"/fruits/?model=efficientnet"}
          btnIcon={Codesandbox}
          cardName="EfficientNet"
          imgSrc={"/images/efficientnet.jpg"}
          nameBg="#cbd5e1"
          nameColor="#334155"
        />
      </section>
    </section>
  );
}

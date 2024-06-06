"use client";
import Card from "../_components/card/card";
import styles from "./page.module.css";

import { ArrowRight } from "react-feather";
import { useSearchParams } from "next/navigation";

export default function Page() {
  const searchParams = useSearchParams();
  const model = searchParams.get("model");
  return (
    <section className={styles.container}>
      <h1 className={styles.pageTitle}>Escolha a Fruta</h1>
      <section className={styles.cardContainer}>
        <Card
          btnHref={`/classification/?model=${model}&fruit=morango`}
          btnIcon={ArrowRight}
          cardName="Morango"
          imgSrc={"/images/strawberry.jpg"}
          nameColor="#dc2626"
          nameBg="#fecaca"
        />
        <Card
          btnHref={`/classification/?model=${model}&fruit=pessego`}
          btnIcon={ArrowRight}
          cardName="Pêssego"
          imgSrc={"/images/peach.jpg"}
          nameBg="#fed7aa"
          nameColor="#f97316"
        />
        <Card
          btnHref={`/classification/?model=${model}&fruit=roma`}
          btnIcon={ArrowRight}
          cardName="Romã"
          imgSrc={"/images/pomegranate.jpg"}
          nameBg="#f87171"
          nameColor="#b91c1c"
        />
      </section>
    </section>
  );
}

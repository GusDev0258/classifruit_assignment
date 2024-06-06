import Image from "next/image";
import { ElementType } from "react";
import Button from "../button/button";
import styles from "./card.module.css";
interface CardProps {
  cardName: string;
  imgSrc: string;
  btnIcon: ElementType;
  btnHref: string;
  nameBg: string;
  nameColor: string;
}
export default function Card({
  cardName,
  imgSrc,
  btnIcon,
  btnHref,
  nameBg,
  nameColor,
}: CardProps) {
  return (
    <article className={styles.container}>
      <section className={styles.imgContainer}>
        <Image
          src={imgSrc}
          alt="Image"
          width={280}
          height={220}
          className={styles.cardImg}
        />
      </section>
      <section className={styles.nameContainer}>
        <h1
          className={styles.name}
          style={{ backgroundColor: nameBg, color: nameColor }}
        >
          {cardName}
        </h1>
      </section>
      <section className={styles.btnContainer}>
        <Button href={btnHref} icon={btnIcon} text="Escolher" />
      </section>
    </article>
  );
}

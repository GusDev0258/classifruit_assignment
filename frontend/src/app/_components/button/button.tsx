import { ElementType, ReactNode } from "react";
import styles from "./button.module.css";
import Link from "next/link";
interface ButtonProps {
  text: string;
  icon: ElementType;
  href: string;
}
export default function Button({ text, icon: Icon, href }: ButtonProps) {
  return (
    <Link href={href}>
      <button className={styles.primaryButton} type="button">
        {text}
        <Icon />
      </button>
    </Link>
  );
}

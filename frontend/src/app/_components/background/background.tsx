import { ReactNode } from "react";
import styles from "./background.module.css";
export default function Background({
  children,
}: Readonly<{ children: ReactNode }>) {
  return (
    <div className={styles.imageContainer}>
      <div className={styles.contentContainer}>
        <div className={styles.content}>{children}</div>
      </div>
    </div>
  );
}

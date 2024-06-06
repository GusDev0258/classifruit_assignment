import Image from "next/image";
import Link from "next/link";
import styles from "./header.module.css";

export default function Header() {
  return (
    <header className={styles.menuContainer}>
      <nav>
        <ul className={styles.menu}>
          <li>
            <Link href={"/"}>
              <Image
                src={"/logo.svg"}
                alt="ClassiFruit Logo"
                width={242}
                height={84}
              />
            </Link>
          </li>
          <div className={styles.menuLinks}>
            <li>
              <Link href={"/models"}>Modelos</Link>
            </li>
            <li>
              <Link href={"/fruits"}>Frutas</Link>
            </li>
          </div>
        </ul>
      </nav>
    </header>
  );
}

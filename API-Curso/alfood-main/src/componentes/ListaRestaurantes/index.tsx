import { useEffect } from "react";
import IRestaurante from "../../interfaces/IRestaurante";
import style from "./ListaRestaurantes.module.scss";
import Restaurante from "./Restaurante";
import axios from "axios";

const ListaRestaurantes = () => {
  const restaurantes: IRestaurante[] = [];

  useEffect(() => {
    axios
      .get("URL")
      .then((resposta) => {
        console.log(resposta);
      })
      .catch((erro) => {
        console.log(erro);
      });
  });

  return (
    <section className={style.ListaRestaurantes}>
      <h1>
        Os restaurantes mais <em>bacanas</em>!
      </h1>
      {restaurantes?.map((item) => (
        <Restaurante restaurante={item} key={item.id} />
      ))}
    </section>
  );
};

export default ListaRestaurantes;

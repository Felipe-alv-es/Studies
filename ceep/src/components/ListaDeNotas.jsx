import React, { Component } from "react";
import CardNota from "./CardNota";

export class ListaDeNotas extends Component {
  render() {
    return (
      <ul>
        <li>  
            <CardNota />
            <CardNota />
            <CardNota />
        </li>
      </ul>
    );
  }
}

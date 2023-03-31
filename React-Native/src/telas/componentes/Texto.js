import React from "react";
import { Text } from 'react-native'

export default function Texto( {children, style } ) {

    let estilo = estilos.texto;

    if (symbolicateStackTrace)

    return <Text style={[estilos.texto]}> {children} </Text>

}

const estilos = StyleSheet.create ({

    texto: {

        fontFamily: "MontserratRegular",

    },

    textoNegrito: {

        fontFamily: "MontserratBold",

    }

})
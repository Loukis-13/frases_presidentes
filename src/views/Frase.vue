<script setup lang="ts">
import { useRoute } from "vue-router";

const presidentes = ["dilma", "lula", "bolsonaro", "temer"]
let presidente = useRoute().params.presidente

if (presidente == 'aleatorio')
  presidente = presidentes[Math.floor(Math.random() * 4)];

const frases = (await import(`../assets/presidentes/${presidente}.js`)).default
const frase = frases[Math.floor(Math.random() * frases.length)]
</script>

<template>
  <body>
    <img :src="`img/${presidente}.jpg`" alt="">
    <p id="frase">{{ frase }}</p>
  </body>
</template>

<script setup lang="ts">
import { capitalize } from 'vue';

const presidentes = ["dilma", "lula", "bolsonaro", "temer", "aleatorio"]
let escolhido = presidentes[Math.floor(Math.random() * 4)];
</script>

<template>

  <body>
    <img :src="`img/${escolhido}.jpg`" alt="">
    <h1>Frases cômicas dos presidentes</h1>

    <select v-model="escolhido">
      <option v-for="presidente in presidentes" :value="presidente" :selected="presidente == escolhido">{{ capitalize(presidente) }}</option>
    </select>
    <button @click="$router.push(escolhido)">Ir</button>

    <p><a id="git" href="https://github.com/Loukis-13/frases_presidentes">GITHUB</a></p>

    <code>este serviço não tem o objetivo de difamar ou apoiar figuras politicas, apenas repassar frases ditas pelos mesmos.</code>
  </body>
</template>

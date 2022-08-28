import { createRouter, createWebHistory } from "vue-router";
import Index from "../views/Index.vue";
import Frase from "../views/Frase.vue";

const presidentes = ["dilma", "lula", "bolsonaro", "temer", "aleatorio"]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: Index },
    { path: `/:presidente(${presidentes.join("|")})`, component: Frase },
    { path: "/:pathMatch(.*)*", redirect: "/" },
  ],
});

export default router;

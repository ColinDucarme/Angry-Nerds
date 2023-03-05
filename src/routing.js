import { createRouter, createWebHistory } from "vue-router";

import MainMenu from './MainMenu.vue';
import Game from './Game.vue';
import Rules from './Rules.vue';

const routes = [
    {
        path: '/',
        component: MainMenu,
    },
    {
        path: '/Game',
        component: Game,
    },
    {
        path: '/Rules',
        component: Rules,
    },
    {
        path: '/:notFound(.*)',
        component: MainMenu,
    }
];

export default createRouter({
    history: createWebHistory(),
    routes,
});
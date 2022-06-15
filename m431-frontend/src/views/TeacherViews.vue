<template>
<!--
  Autheur:        Théo Ribbi & Nadir Serhir 
  Projet:         Gestioonie
  Description:    Plateforme pour la gestion de vie scolaire (Faite pour le Module 431)
  Composant:      TeacherView.vue
  Date:           13.06.2022
  Version:        1.0
-->
  <div class="teacher">
        <div>     
        <div v-if="token == null" class="flex h-screen bg-gray-200">
            Vous n'avez pas la permissions d'accéder à cette page
        </div>   
        <div v-if="token != null" class="flex h-screen bg-gray-200">
            <div class="flex-1 flex flex-col overflow-hidden">
                <main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200">
                    <div class="container mx-auto px-6 py-8">
                        <h3 class="text-gray-700 text-3xl font-medium">Bienvenue {{userInfo.first_name}} </h3>
                        <div class="mt-4">
                            <div class="flex flex-wrap -mx-6">
                                <div class="w-full px-6 sm:w-1/2 xl:w-1/3">
                                    <div class="flex items-center px-5 py-6 shadow-sm rounded-md bg-white">
                                        <div class="p-3 rounded-full bg-indigo-600 bg-opacity-75">
                                            <svg class="h-8 w-8 text-white" viewBox="0 0 28 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M18.2 9.08889C18.2 11.5373 16.3196 13.5222 14 13.5222C11.6804 13.5222 9.79999 11.5373 9.79999 9.08889C9.79999 6.64043 11.6804 4.65556 14 4.65556C16.3196 4.65556 18.2 6.64043 18.2 9.08889Z" fill="currentColor"></path>
                                                <path d="M25.2 12.0444C25.2 13.6768 23.9464 15 22.4 15C20.8536 15 19.6 13.6768 19.6 12.0444C19.6 10.4121 20.8536 9.08889 22.4 9.08889C23.9464 9.08889 25.2 10.4121 25.2 12.0444Z" fill="currentColor"></path>
                                                <path d="M19.6 22.3889C19.6 19.1243 17.0927 16.4778 14 16.4778C10.9072 16.4778 8.39999 19.1243 8.39999 22.3889V26.8222H19.6V22.3889Z" fill="currentColor"></path>
                                                <path d="M8.39999 12.0444C8.39999 13.6768 7.14639 15 5.59999 15C4.05359 15 2.79999 13.6768 2.79999 12.0444C2.79999 10.4121 4.05359 9.08889 5.59999 9.08889C7.14639 9.08889 8.39999 10.4121 8.39999 12.0444Z" fill="currentColor"></path>
                                                <path d="M22.4 26.8222V22.3889C22.4 20.8312 22.0195 19.3671 21.351 18.0949C21.6863 18.0039 22.0378 17.9556 22.4 17.9556C24.7197 17.9556 26.6 19.9404 26.6 22.3889V26.8222H22.4Z" fill="currentColor"></path>
                                                <path d="M6.64896 18.0949C5.98058 19.3671 5.59999 20.8312 5.59999 22.3889V26.8222H1.39999V22.3889C1.39999 19.9404 3.2804 17.9556 5.59999 17.9556C5.96219 17.9556 6.31367 18.0039 6.64896 18.0949Z" fill="currentColor"></path>
                                            </svg>
                                        </div>
                                        <div class="mx-5">
                                            <h4 class="text-2xl font-semibold text-gray-700">{{ userList.length }} </h4>
                                            <div class="text-gray-500">Eleves</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="mt-8">
                        </div>
                        <div class="flex flex-col mt-8">
                            <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
                                <div class="align-middle inline-block min-w-full shadow overflow-hidden sm:rounded-lg border-b border-gray-200">
                                    <table class="min-w-full">
                                        <thead>
                                            <tr>
                                                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                                                    Nom et prénom
                                                </th>
                                                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                                                    Ajouter appréciations
                                                </th>
                                                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                                                    Date de l'appréciations
                                                </th>
                                                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                                                    Envoyez l'appréciations
                                                </th>
                                            </tr>
                                        </thead>
        
                                        <tbody class="bg-white">
                                            <tr v-bind:key="userList.id" v-for="userList in userList">
                                                <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                                                    <div class="flex items-center">
                                                        <div class="ml-4">
                                                            <div class="text-sm leading-5 font-medium text-gray-900"> {{ userList.first_name }} {{ userList.last_name }}
                                                            </div>
                                                            <div class="text-sm leading-5 text-gray-500">{{userList.email}}</div>
                                                        </div>
                                                    </div>
                                                </td>
        
                                                <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                                                    <div class="text-sm leading-5 text-gray-900"></div>
                                                    <select v-model="observationSelected" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                                    <option v-for="observationList in observationList" v-bind:key="observationList.id">{{observationList.title}}</option>
                                                    </select>
                                                </td>
                                                <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                                                   <input v-model="observationDate" type="datetime-local" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                                </td>
                                                <td class="px-6 py-4 whitespace-no-wrap border-b flex justify-center border-gray-200">
                                                   <button @click="sendAppreciation(userList), sendAppreciationConfirm = true" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">
                                                        Envoyez
                                                    </button>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <div v-if="sendAppreciationConfirm" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
                                        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                                        <div class="fixed inset-0  bg-gray-500 bg-opacity-75  transition-opacity" aria-hidden="true"></div>
                                        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true" >&#8203;</span>
                                        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                                            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                                            <div class="sm:flex sm:items-start">
                                                <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-green-300 sm:mx-0 sm:h-10 sm:w-10">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M20.285 2l-11.285 11.567-5.286-5.011-3.714 3.716 9 8.728 15-15.285z"/></svg>
                                                </div>
                                                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                                                <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                                                    Informations
                                                </h3>
                                                <div class="mt-2">
                                                    <p class="text-sm text-gray-500">
                                                   L'appréciation à bien été envoyée
                                                    </p>
                                                </div>
                                                </div>
                                            </div>
                                            </div>
                                            <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                                            <button @click="sendAppreciationConfirm = false" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                                                Ok
                                            </button>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"; // Librairie pour utiliser les API's

export default {
  name: "App",

  data: () => ({
    sendAppreciationConfirm: false,
    isLogged: null, 
    token: null,
    user_id_cache: null,
    user_first_name_cache: null,
    user_last_name_cache: null,
    userInfo: {},
    userList: {},
    observationList: {},
    selectedList: {},
    observationSelected: null,
    username: null,
    observationDate: null,
    apiUser: "http://127.0.0.1:8003/profile/user",
    apiUserId: "http://127.0.0.1:8003/profile/user/",
    apiObservation: "http://127.0.0.1:8003/observation",
    apiAppreciation: "http://127.0.0.1:8003/appreciations",
  }),

  methods: {

    sendAppreciation(userList){

    // Condition pour remplacer le text par l'ID
    if (this.observationSelected == "Absence non excusée") {
        this.observationSelected = 3
    } 

    if (this.observationSelected == "Absence Excusée") {
        this.observationSelected = 4
    } 

    if (this.observationSelected == "Arrivé Tardive") {
        this.observationSelected = 5
    } 

    if (this.observationSelected == "Renvoi") {
        this.observationSelected = 6
    } 

    if (this.observationSelected == "Devoir non fait") {
        this.observationSelected = 7
    } 
    
    if (this.observationSelected == "Oublie") {
        this.observationSelected = 8
    } 

    // Variable avec les informations pour transmettre a l'API
    var userInfoAPI = {
        date_time: this.observationDate,
        appreciation: this.observationSelected,
        user: userList.id
    }

    // Appelle post vers l'API
    axios.post(this.apiAppreciation, userInfoAPI).then(response => { 
      console.log('response');
      console.log(response);
    });
    },

  },


  mounted() {
    this.token = localStorage.getItem('token'); // Token de l'API d'authentification (Définit dans le comp. AccountLogin.vue) et le prend depuis le cache
    this.user_id_cache = localStorage.getItem('user.id'); // ID de l'utilisateur (Définit dans le comp. AccountLogin.vue) et le prend depuis le cache
    this.user_first_name_cache = localStorage.getItem('user.first_name'); // Prenom de l'utilisateur (Définit de le comp. AccountLogin.vue) et le prend depuis le cache
    this.user_last_name_cache = localStorage.getItem('user.last_name'); // Nom de famille de l'utilisateur (Définit dans le comp. AccountLogin.vue) et le stock dans le navigateur
    axios.get(this.apiUser).then((response) => (this.userList = response.data)); // GET du endpoint de l'API User
    axios.get(this.apiObservation).then((response) => (this.observationList = response.data)); // GET du endpoint de l'API Observation
    axios.get(this.apiUserId + this.user_id_cache).then((response) => (this.userInfo = response.data)); // GET du endpoint de l'API User et de l'id de l'utilisateur
    
   
  },
};
</script>
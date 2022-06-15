<template>
<!--
  Autheur:        Théo Ribbi & Nadir Serhir 
  Projet:         Gestioonie
  Description:    Plateforme pour la gestion de vie scolaire (Faite pour le Module 431)
  Composant:      AccountLogin.vue
  Date:           13.06.2022
  Version:        1.0
-->
  <div class="login">
  <section class="h-full gradient-form bg-gray-200 md:h-screen">
  <div class="container py-12 px-6 h-full">
    <div class="flex justify-center items-center flex-wrap h-full g-6 text-gray-800">
      <div class="xl:w-10/12">
        <div class="block bg-white shadow-lg rounded-lg">
          <div class="lg:flex lg:flex-wrap g-0">
            <div class="lg:w-6/12 px-4 md:px-0">
              <div class="md:p-12 md:mx-6">
                <div class="text-center">
                  <!-- <img class="mx-auto w-48" src="" alt="logo"/> -->
                  <h4 class="text-xl font-semibold mt-1 mb-12 pb-1">Gestioonie</h4>
                </div>
                <form>
                  <p class="mb-4">Connectez-vous à votre compte</p>
                  <div class="mb-4">
                    <input v-if="isLogged == null" v-model="userMail" type="email" class="form-control block w-full px-3 py-1.5 text-base font-normal text-grey-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleFormControlInput1" placeholder="Email"/>
                    <input v-if="isLogged == false" v-model="userMail" type="email" class="form-control block w-full px-3 py-1.5 text-base font-normal text-red-700 bg-red bg-clip-padding border border-solid border-red-700 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleFormControlInput1" placeholder="Email"/>
                  </div>
                  <input v-if="isLogged == null" v-model="userPassword" type="password" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleFormControlInput1" placeholder="Mot de passe"/>
                  <input v-if="isLogged == false" v-model="userPassword" type="password" class="form-control block w-full px-3 py-1.5 text-base font-normal text-red-700 bg-white bg-clip-padding border border-solid border-red-700 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleFormControlInput1" placeholder="Mot de passe"/>
                  <div v-if="isLogged == false" class="inline-flex items-center w-full p-4 mb-4 mt-2 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800" role="alert">
                    <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="times-circle" class="w-4 h-4 mr-2 fill-current" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                      <path fill="currentColor" d="M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm121.6 313.1c4.7 4.7 4.7 12.3 0 17L338 377.6c-4.7 4.7-12.3 4.7-17 0L256 312l-65.1 65.6c-4.7 4.7-12.3 4.7-17 0L134.4 338c-4.7-4.7-4.7-12.3 0-17l65.6-65-65.6-65.1c-4.7-4.7-4.7-12.3 0-17l39.6-39.6c4.7-4.7 12.3-4.7 17 0l65 65.7 65.1-65.6c4.7-4.7 12.3-4.7 17 0l39.6 39.6c4.7 4.7 4.7 12.3 0 17L312 256l65.6 65.1z"></path>
                    </svg>
                    <span class="font-medium">Erreur!</span><span>&nbsp;Vérifier vos informations de connections. </span>
                  </div>
                  <div class="mb-4">
                  </div>
                  <div class="text-center pt-1 mb-12 pb-1">
                    <button v-if="isLogged == null" @click="loginAuthToken()" class="inline-block px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3" type="button" data-mdb-ripple="true" data-mdb-ripple-color="light" style="background: linear-gradient(to right, #6F00FF, #7A36D2, #8D5CCD, #997FBA);">
                      Se connecter !
                    </button>
                    <button v-if="isLogged == false" @click="loginAuthToken()" class="inline-block px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-900 hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3" type="button" data-mdb-ripple="true" data-mdb-ripple-color="light" style="background: linear-gradient(to right, #FF0000, #FD3434, #FF6565, #FDA2A2);">
                      Se connecter !
                    </button>
                    <a @click="isForgotPassword =! isForgotPassword" class="text-gray-500">Mot de passe oublié ?</a>
                  </div>
                  <div class="flex items-center justify-between pb-6">
                    <p class="mb-0 mr-2">Vous n'avez pas de compte ?</p>
                    <button @click="isNotActivate =! isNotActivate" v-if="isLogged == null" type="button" class="inline-block px-6 py-2 border-2 border-violet-600 text-violet-600 font-medium text-xs leading-tight uppercase rounded hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 transition duration-150 ease-in-out" data-mdb-ripple="true" data-mdb-ripple-color="light">
                      Cliquez ici
                    </button>
                    <button @click="isNotActivate =! isNotActivate" v-if="isLogged == false" type="button" class="inline-block px-6 py-2 border-2 border-red-700  text-red-700 font-medium text-xs leading-tight uppercase rounded hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 transition duration-150 ease-in-out" data-mdb-ripple="true" data-mdb-ripple-color="light">
                      Cliquez ici
                    </button>
                  </div>
                </form>
              </div>
            </div>
            <div v-if="isLogged == null" class="lg:w-6/12 flex items-center lg:rounded-r-lg rounded-b-lg lg:rounded-bl-none" style="background: linear-gradient(to right, #6F00FF, #7A36D2, #8D5CCD, #997FBA);">
              <div class="text-white px-4 py-6 md:p-12 md:mx-6">
                <h4 class="text-xl font-semibold mb-6">Garder une vue sur votre vie scolaire</h4>
                <p class="text-sm">
                 Avoir Gestioonie avec soi c'est pouvoir constater une évolution en temps réel et ne pas comparer bulletin après bulletin. 
                 <br> Pouvoir avoir Gestioonie avec soi permet de se mettre à soi-même une certaine pression directe et ne pas attendre la fin d'un semestre et échouer.
                 <br> Avoir Gestioonie avec soi c'est réussir.
                </p>
              </div>
            </div>
            <div v-if="isLogged == false" class="lg:w-6/12 flex items-center lg:rounded-r-lg rounded-b-lg lg:rounded-bl-none" style="background: linear-gradient(to right, #FF0000, #FD3434, #FF6565, #FDA2A2);">
              <div class="text-white px-4 py-6 md:p-12 md:mx-6">
                <h4 class="text-xl font-semibold mb-6">Garder une vue sur votre vie scolaire</h4>
                <p class="text-sm">
                  Avoir Gestioonie avec soi c'est pouvoir constater une évolution en temps réel et ne pas comparer bulletin après bulletin. 
                 <br> Pouvoir avoir Gestioonie avec soi permet de se mettre à soi-même une certaine pression directe et ne pas attendre la fin d'un semestre et échouer.
                 <br> Avoir Gestioonie avec soi c'est réussir.
                </p>
              </div>
            </div>
            <div v-if="isForgotPassword == true">
                <div v-if="isForgotPassword" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
                  <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
                    <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
                    <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                      <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                        <div class="sm:flex sm:items-start">
                          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><path d="M12 5.177l8.631 15.823h-17.262l8.631-15.823zm0-4.177l-12 22h24l-12-22zm-1 9h2v6h-2v-6zm1 9.75c-.689 0-1.25-.56-1.25-1.25s.561-1.25 1.25-1.25 1.25.56 1.25 1.25-.561 1.25-1.25 1.25z"/></svg>
                          <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                              Attention
                            </h3>
                            <div class="mt-2">
                              <p class="text-sm text-gray-500">
                                Veuillez-contactez un professeur pour changez votre mot de passe
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                        <button @click="isForgotPassword = false" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                          Ok
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
          </div>
          <div v-if="isNotActivate == true">
            <div v-if="isNotActivate" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
              <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
                <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
                <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                  <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><path d="M12 5.177l8.631 15.823h-17.262l8.631-15.823zm0-4.177l-12 22h24l-12-22zm-1 9h2v6h-2v-6zm1 9.75c-.689 0-1.25-.56-1.25-1.25s.561-1.25 1.25-1.25 1.25.56 1.25 1.25-.561 1.25-1.25 1.25z"/></svg>
                      <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                        <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                          Attention
                        </h3>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">
                            Veuillez-contactez un professeur pour activer votre compte
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                    <button @click="isNotActivate = false" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
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
  </div>
</section>
</div>
</template>

<script>
import axios from "axios"; // Librairie pour utiliser les API's

export default {
  name: "App",

  data: () => ({
    userMail: "",
    userPassword: "",
    apiAuthToken: "http://127.0.0.1:8003/api-token-auth/",
    isLogged: null,
    isForgotPassword: "false",
    isNotActivate: "false",
  }),

  methods: {
    // Login avec l'API
    loginAuthToken() {
      const loginInfo = {
        username: this.userMail,
        password: this.userPassword,
      }
      // Appelle à l'API
      axios.post(this.apiAuthToken, loginInfo).then((response) => {
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user.id', response.data.user.id);
        localStorage.setItem('user.first_name', response.data.user.first_name);
        localStorage.setItem('user.last_name', response.data.user.last_name);
        console.log(response.data)
         console.log("then")
         // Met la variable a true
         this.isLogged = true
         // Si la variable est true alors redirection
         if (this.isLogged == true) {
           this.$router.push({ path: '/redirect' })
         }
      }).catch(() => { // Si le login est pas bon alors
        this.isLogged = false
      }); 
    },
  },
};
</script>
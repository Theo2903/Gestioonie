<template>
<!--
  Autheur:        Théo Ribbi & Nadir Serhir 
  Projet:         Gestioonie
  Description:    Plateforme pour la gestion de vie scolaire (Faite pour le Module 431)
  Composant:      RedirectToViews.vue
  Date:           13.06.2022
  Version:        1.0
-->
  <div class="login">
    <div v-if="token == null" class="flex h-screen bg-gray-200">
        Vous n'avez pas la permissions d'accéder à cette page
    </div>
  <section v-if="token != null" class="h-full gradient-form bg-gray-200 md:h-screen">
  <div class="container py-12 px-6 h-full">
    <div class="flex justify-center items-center flex-wrap h-full g-6 text-gray-800">
      <div class="xl:w-10/12">
        <div class="block bg-white shadow-lg rounded-lg">
          <div class="lg:flex lg:flex-wrap g-0">
            <div class="lg:w-6/12 px-4 md:px-0">
              <div class="md:p-12 md:mx-6">
                <div class="text-center">
                  <h4 class="text-xl font-semibold mt-1 mb-12 pb-1">Gestioonie</h4>
                </div>
                <form>
                  <p class="mb-4">Choissez votre page</p>
                    <button @click="redirectToStudent()" class="inline-block px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3" type="button" data-mdb-ripple="true" data-mdb-ripple-color="light" style="background: linear-gradient(to right, #6F00FF, #7A36D2, #8D5CCD, #997FBA);">
                      Portail Elève
                    </button>
                    <button @click="redirectToTeacher()" class="inline-block px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3" type="button" data-mdb-ripple="true" data-mdb-ripple-color="light" style="background: linear-gradient(to right, #6F00FF, #7A36D2, #8D5CCD, #997FBA);">
                      Portail Professeur
                    </button>
                </form>
              </div>
            </div>
            <div class="lg:w-6/12 flex items-center lg:rounded-r-lg rounded-b-lg lg:rounded-bl-none" style="background: linear-gradient(to right, #6F00FF, #7A36D2, #8D5CCD, #997FBA);">
              <div class="text-white px-4 py-6 md:p-12 md:mx-6">
                <h4 class="text-xl font-semibold mb-6">Garder une vue sur votre vie scolaire</h4>
                <p class="text-sm">
                 Avoir Gestioonie avec soi c'est pouvoir constater une évolution en temps réel et ne pas comparer bulletin après bulletin. 
                 <br> Pouvoir avoir Gestioonie avec soi permet de se mettre à soi-même une certaine pression directe et ne pas attendre la fin d'un semestre et échouer.
                 <br> Avoir Gestioonie avec soi c'est réussir.
                </p>
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

export default {
  name: "App",

  data: () => ({
    token: null,
  }),

  methods: {
    // Redirection vers la page élève 
    redirectToStudent(){
        this.$router.push({ path: '/student' })
    },

    // Redirection vers la page professeur
    redirectToTeacher(){
        this.$router.push({ path: '/teacher' })
    },
  },

  mounted() {
    this.token = localStorage.getItem('token'); // Token de l'API d'authentification (Définit dans le comp. AccountLogin.vue) et le prend depuis le cache
  }
};
</script>
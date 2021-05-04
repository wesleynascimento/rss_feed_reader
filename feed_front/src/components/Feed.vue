<template>
  <div id="app">
    <div class="container">
      <form @submit.prevent="salvar" class="right-aligned">
        <div>
          <label>Nome</label>
          <input type="text" placeholder="Nome" v-model="site.name" />
        </div>
        <div>
          <label>Url</label>
          <input type="text" placeholder="Url" v-model="site.site_url" />
        </div>
        <label>Categoria</label>
        <input type="text" placeholder="Categoria" v-model="site.category" />

        <button class="waves-effect waves-light btn-small">Salvar</button>
      </form>

      <md-layout>
        <md-layout md-row>
          <md-layout
            v-for="site in sites"
            :key="site.id"
            md-flex="33"
            md-align="center"
          >
            <md-card md-with-hover class="card">
              <md-card-header>
                <div class="md-title">{{ site.name }}</div>
              </md-card-header>

              <md-card-content>
                {{ site.site_url }}
              </md-card-content>

              <md-card-actions>
                <md-button @click="getFeed(site)">Ir para o Feed</md-button>
              </md-card-actions>
              <br />
            </md-card>
          </md-layout>
        </md-layout>
      </md-layout>
    </div>
  </div>
</template>

<script>
import Feed from "@/services/api/index";
export default {
  data() {
    return {
      site: {
        name: "",
        site_url: "",
        category: "",
      },
      sites: [],
    };
  },

  mounted() {
    this.listar();
  },

  methods: {
    listar() {
      Feed.listar().then((resposta) => {
        this.sites = resposta.data;
        console.log(resposta);
      });
    },

    salvar() {
      Feed.salvar(this.site);
    },
    getFeed: function (site) {
      this.$router.push({ name: "News", params: { feed_name: site.name } });
    },
  },
};
</script>

<style scoped>
.card {
  width: 90%;
  margin-bottom: 30px;
}
input {
  display: block;
  margin: 0 auto;
  width: 250px;
}

form {
  padding: 20px;
}
</style>

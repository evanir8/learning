<template>
  <div>
   <h1>{{ titulo }}</h1>
  <ul>
  <li v-for="foto of fotos">
    <img :src="foto.url" :alt="foto.titulo">
  </li>
  </ul>
</div>
</template>

<script>
export default {
  data() {
    return {
      titulo: 'EsferaPic',
      fotos: [
      {
        url: 'https://img.ibxk.com.br/2019/07/26/26000559344397.jpg?w=1120&h=420&mode=crop&scale=both',
        titulo: 'Eclipse'
      },
      {
        url: 'https://imagens.canaltech.com.br/236607.471195-Lua.jpg',
        titulo: 'Lua'
      }
      ]
    }
  }
  //created(){
 // }
}

</script>

<style>

</style>

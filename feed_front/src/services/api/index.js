import { http } from "./config";

export default {
  listar: () => {
    return http.get("feed");
  },

  salvar: (site) => {
    http.post("feed", {
      name: site.name,
      site_url: site.site_url,
      category: site.category,
    });
    alert("salvo com sucesso!");
  },
};

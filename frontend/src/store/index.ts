import { defineStore } from "pinia";
import { ref } from "vue";

export const useAppStore = defineStore("app", () => {
  const projectName = ref("OpenFDAMS");
  const version = ref("0.0.4");
  const loading = ref(false);

  return { projectName, version, loading };
});

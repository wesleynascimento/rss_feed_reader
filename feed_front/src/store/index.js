import Vue from 'vue';
import Vuex from 'vuex';
import { loginUser, logoutUser } from '../services/api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: false,
  },
  mutations: {
    loginSuccess(state, userId) {
      state.user = userId;
      state.isLoggedIn = true;
    },
    logout(state) {
      state.user = null;
      state.isLoggedIn = false;
    },
  },
  actions: {
    login({ commit }, { email, password }) {
      return loginUser(email, password)
        .then(() => {
          commit({ type: 'loginSuccess', email });
          return Promise.resolve();
        }).catch((error) => {
          commit({ type: 'logout' });
          return Promise.reject(error);
        });
    },
    logout({ commit }) {
      logoutUser();
      commit('logout');
    },
  },
  modules: {

  },
});

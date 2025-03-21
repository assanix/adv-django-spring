<template>
  <v-container class="d-flex justify-center align-center" style="min-height: 100vh;">
    <v-card class="pa-6" max-width="450" elevation="3">
      <v-card-title class="text-h5 font-weight-bold justify-center">
        📝 Register
      </v-card-title>

      <v-card-text>
        <v-form @submit.prevent="register" ref="form" lazy-validation>
          <v-text-field
            v-model="username"
            label="👤 Username"
            outlined
            dense
            required
          ></v-text-field>

          <v-text-field
            v-model="email"
            label="📧 Email"
            outlined
            dense
            required
            type="email"
          ></v-text-field>

          <v-select
            v-model="role"
            :items="roles"
            label="🎭 Role"
            outlined
            dense
            required
          ></v-select>

          <v-text-field
            v-model="password"
            label="🔑 Password"
            outlined
            dense
            required
            type="password"
          ></v-text-field>

          <v-text-field
            v-model="password2"
            label="🔒 Confirm Password"
            outlined
            dense
            required
            type="password"
          ></v-text-field>

          <v-btn
            color="primary"
            type="submit"
            class="mt-4"
            block
            elevation="1"
          >
            Register
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserRegister',
  data() {
    return {
      username: '',
      email: '',
      role: 'user',
      roles: ['user', 'admin'],
      password: '',
      password2: '',
    };
  },
  methods: {
    async register() {
      try {
        await axios.post('http://127.0.0.1:8000/api/register/', {
          username: this.username,
          email: this.email,
          role: this.role,
          password: this.password,
          password2: this.password2,
        });
        this.$router.push('/');
      } catch (error) {
        console.error('Registration failed:', error);
      }
    },
  },
};
</script>

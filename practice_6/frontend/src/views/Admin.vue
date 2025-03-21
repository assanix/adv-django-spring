<template>
  <v-container>
    <v-card class="pa-4 elevation-2">
      <v-card-title class="d-flex justify-space-between align-center">
        <span class="text-h6">⚙️ Admin Panel</span>
        <v-btn color="red darken-1" @click="logout" elevation="1" rounded>Logout</v-btn>
      </v-card-title>

      <v-divider class="my-2"></v-divider>

      <v-table class="elevation-1">
        <thead>
          <tr>
            <th class="text-left">📛 Name</th>
            <th class="text-left">📝 Description</th>
            <th class="text-left">🧩 Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.id">
            <td>{{ item.name }}</td>
            <td>{{ item.description }}</td>
            <td>
              <v-btn color="red" variant="tonal" @click="deleteItem(item.id)" small>
                Delete
              </v-btn>
            </td>
          </tr>
        </tbody>
      </v-table>
    </v-card>
  </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
    };
  },
  computed: {
    ...mapState(['token']),
  },
  async created() {
    const response = await axios.get('http://127.0.0.1:8000/api/items/', {
      headers: { Authorization: `Bearer ${this.token}` },
    });
    this.items = response.data;
  },
  methods: {
    ...mapActions(['logout']),
    async deleteItem(id) {
      await axios.delete(`http://127.0.0.1:8000/api/items/${id}/`, {
        headers: { Authorization: `Bearer ${this.token}` },
      });
      this.items = this.items.filter(item => item.id !== id);
    },
  },
};
</script>

<style scoped>
.v-table {
  border-radius: 10px;
  overflow: hidden;
}

td {
  vertical-align: middle;
}
</style>

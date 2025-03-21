<template>
  <div class="container">
    <h1 class="title">📦 Items</h1>

    <ul class="item-list">
      <li v-for="item in items" :key="item.id" class="item">
        <strong>{{ item.name }}</strong><br />
        <span class="description">{{ item.description }}</span>
      </li>
    </ul>

    <form @submit.prevent="addItem" class="form">
      <input v-model="newItem.name" placeholder="Item name" required class="input" />
      <input v-model="newItem.description" placeholder="Description" required class="input" />
      <button type="submit" class="button">Add Item</button>
    </form>
  </div>
</template>

<script>
import { getItems, createItem } from '../api';

export default {
  data() {
    return {
      items: [],
      newItem: { name: '', description: '' },
    };
  },
  async created() {
    this.items = await getItems();
  },
  methods: {
    async addItem() {
      const item = await createItem(this.newItem);
      this.items.push(item);
      this.newItem = { name: '', description: '' };
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.title {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
}

.item-list {
  list-style: none;
  padding: 0;
  margin-bottom: 30px;
}

.item {
  background: #f1f1f1;
  padding: 15px 20px;
  border-radius: 10px;
  margin-bottom: 10px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.description {
  color: #555;
  font-size: 0.9rem;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
}

.button {
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button:hover {
  background-color: #2c8c6f;
}
</style>

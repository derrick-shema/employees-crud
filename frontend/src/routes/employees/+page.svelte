<script lang="ts">
	import { onMount } from "svelte";
  type Employee = {
    id: number;
    first_name: string;
    last_name: string;
    title: string;
  };

  let employees: Employee[] = [];

  async function fetchEmployees() {
    const res = await fetch('http://localhost:8000/api/employees');
    employees = await res.json();
  }
  async function handleDelete(id: number) {
    await fetch(`http://localhost:8000/api/employees/${id}`, {
      method: 'DELETE'
    });
    await fetchEmployees();
  }

  onMount(fetchEmployees);
</script>
<section>
  <h1 class="text-3xl font-bold text-gray-900 mb-4">Our Awesome Staff</h1>
  <a href="/employees/new" class="bg-blue-700 text-white px-3 py-2 mb-6">Add Employee</a>
  <ul class="mt-6">
  {#each employees as emp (emp.id)}
    <li class="flex items-center justify-between mb-2 p-2 border rounded">
      <span>{emp.first_name} {emp.last_name} — {emp.title}</span>
      <div class="space-x-2">
        <a
          href={`/employees/${emp.id}/edit`}
          class="bg-yellow-500 text-white px-3 py-1 rounded hover:bg-yellow-600 transition"
        >
          Edit
        </a>
        <button
          class="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-800 transition"
          on:click={() => handleDelete(emp.id)}
        >
          Delete
        </button>
      </div>
    </li>
  {/each}
</ul>

</section>
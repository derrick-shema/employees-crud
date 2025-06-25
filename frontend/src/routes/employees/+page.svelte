<script lang="ts">
	import { invalidateAll } from '$app/navigation';

  export let data;
  const employees = data.employees;
  async function handleDelete(id: number) {
    await fetch(`http://localhost:8000/api/employees/${id}`, {
      method: 'DELETE'
    });
    // Refresh the data from the server
    await invalidateAll();
  }
</script>
<section>
  <h1 class="text-3xl font-bold text-gray-900 mb-4">Our Awesome Staff</h1>
  <a href="/employees/new" class="bg-blue-700 text-white px-3 py-2 mb-6">Add Employee</a>
  <ul class="mt-6">
  {#each employees as emp}
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
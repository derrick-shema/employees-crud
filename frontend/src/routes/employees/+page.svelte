<script>
  export let data;
  const employees = data.employees;
</script>
<section>
  <h1 class="text-3xl font-bold text-gray-900 mb-4">Our Awesome Staff</h1>
  <a href="/employees/new" class="bg-blue-700 text-white px-3 py-2 mb-6">Add Employee</a>
  <ul class="mt-6">
  {#each employees as emp}
    <li>{emp.first_name} {emp.last_name} — {emp.title}</li>
  {/each}
</ul>

</section>
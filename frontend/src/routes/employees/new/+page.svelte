<script lang="ts">
	import { goto } from '$app/navigation';
  import EmployeeForm from '$lib/EmployeeForm.svelte';

  type Employee = {
    first_name: string;
    last_name: string;
    title: string;
  };

  // Optionally, you can define a handler for form submission
  async function handleCreate(employee: Employee) {
    // Example: send POST request to your API
    await fetch('http://localhost:8000/api/employees', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(employee)
    });
    // Optionally, redirect or show a success message here
    goto('/employees', {invalidateAll: true});
  }
</script>
<div>
  <h1 class="text-2xl font-bold mb-4">New Employee</h1>
  <EmployeeForm onSubmit={handleCreate} />
</div>


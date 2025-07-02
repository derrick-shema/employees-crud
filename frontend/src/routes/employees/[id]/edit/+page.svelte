<script lang="ts">
  import { onMount } from "svelte";
  import EmployeeForm from '$lib/EmployeeForm.svelte';
  import { page } from '$app/state';
  import { goto } from '$app/navigation';

  type Employee = {
    first_name: string;
    last_name: string;
    title: string;
  };

  let employee: Employee | null = null;
  console.log(employee);
  let id = page.params.id;

  onMount(async () => {
    const res = await fetch(`http://localhost:8000/api/employees/${id}`);
    employee = await res.json();
    console.log(employee);
  });

  async function handleUpdate(updated: Employee) {
    await fetch(`http://localhost:8000/api/employees/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(updated)
    });
    goto('/employees');
  }
</script>

<h1 class="text-2xl font-bold mb-4">Edit Employee</h1>
{#if employee}
  {console.log(employee)}
  <EmployeeForm {employee} onSubmit={handleUpdate} />
{:else}
  <p>Loading...</p>
{/if}
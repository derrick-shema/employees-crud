<script lang="ts">
  type Employee = {
    first_name: string;
    last_name: string;
    title: string;
  };

  export let employee: Employee = { first_name: '', last_name: '', title: '' };
  export let onSubmit: (employee: Employee) => void;

  let form: Employee = { ...employee };

  function handleSubmit(event: Event) {
    event.preventDefault();
    onSubmit(form);
  }
</script>

<form class="max-w-md mx-auto bg-white p-6 rounded shadow" on:submit={handleSubmit}>
  <div class="mb-4">
    <label class="block mb-1 font-semibold" for="first_name">First Name</label>
    <input
      id="first_name"
      class="w-full border rounded px-3 py-2"
      type="text"
      bind:value={form.first_name}
      required
    />
  </div>
  <div class="mb-4">
    <label class="block mb-1 font-semibold" for="last_name">Last Name</label>
    <input
      id="last_name"
      class="w-full border rounded px-3 py-2"
      type="text"
      bind:value={form.last_name}
      required
    />
  </div>
  <div class="mb-4">
    <label class="block mb-1 font-semibold" for="title">Title</label>
    <input
      id="title"
      class="w-full border rounded px-3 py-2"
      type="text"
      bind:value={form.title}
      required
    />
  </div>
  <button
    type="submit"
    class="bg-blue-700 text-white px-4 py-2 rounded hover:bg-blue-900 transition"
  >
    Save
  </button>
</form>
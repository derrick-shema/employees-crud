<script lang="ts">
	import '../app.css';
	import { page } from '$app/state';
	let { children } = $props();
</script>
<div class="px-4 md:px-12">
<header class="flex justify-between mt-0 py-4">
  <div class="flex items-center space-x-3">
  	<img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" alt="Random Logo"  class="h-8 w-8 rounded-full"/>
  	<span class="text-2xl font-bold text-blue-800">AwesomeInc</span>
</div>
  <nav class="">
	<a 
		href="/about" 
		class= {`px-3 py-1 rounded transition hover:bg-blue-100 hover:text-blue-900 text-blue-700 ${
			page.url.pathname === '/about'
      		? 'bg-blue-200 text-blue-900 font-semibold'
      		: 'text-blue-700'
		}`}
	>About</a>
    <a 
		href= '/employees' 
		class= {`px-3 py-1 rounded transition hover:bg-blue-100 hover:text-blue-900 text-blue-700 ${
			page.url.pathname === '/employees'
      		? 'bg-blue-200 text-blue-900 font-semibold'
      		: 'text-blue-700'
		}`}
	>Employees</a>
    
  </nav>
</header>
{@render children()}
</div>

export async function load({ fetch }) {
	const res = await fetch('http://localhost:8000/api/employees');
	if (!res.ok) throw new Error('Failed to fetch employees');
	const employees = await res.json();
	return { employees };
}

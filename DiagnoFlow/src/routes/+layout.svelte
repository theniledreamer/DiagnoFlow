<script>
    let { children } = $props();
</script>

<style>
    nav {
        display: flex;
        align-items: center;
        background-color: #333;
        padding: 1rem 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    nav a {
        color: white;
        text-decoration: none;
        font-size: 1.1rem;
        margin-right: 2rem;
        transition: color 0.3s ease, transform 0.2s ease;
        white-space: nowrap; /* Prevents text wrapping for long links */
    }

    nav a:last-child {
        margin-right: 0; /* No extra space for the last link */
    }

    nav a:hover {
        color: #00d1b2;
        transform: scale(1.1);
    }

    nav a:active {
        color: #ff3860;
    }

    nav a.current {
        color: #00d1b2; /* Highlight active page */
        font-weight: bold;
    }

    /* Responsive Design for Mobile */
    @media (max-width: 768px) {
        nav {
            flex-wrap: wrap; /* Allows wrapping of links for small screens */
            padding: 1rem;
        }

        nav a {
            margin: 0.5rem 1rem;
            font-size: 1rem;
        }
    }

    main {
        padding: 2rem;
    }
</style>

<nav>
    <a href="/" class="current">Sample Entry</a>
    <a href="/batches">Batches</a>

</nav>

<main>
    {@render children()}
</main>

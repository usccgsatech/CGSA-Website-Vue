<template>
    <div>nihao</div>
</template>

<script setup lang="ts">
// Home page component
</script>

<style scoped>
.home {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

.hero-section {
    text-align: center;
    margin-bottom: 4rem;
    padding: 3rem 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 12px;
}

.hero-section h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    font-weight: 700;
}

.subtitle {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    opacity: 0.9;
}

.description {
    font-size: 1.1rem;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.feature-card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border: 1px solid #e5e7eb;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.feature-card h3 {
    color: #374151;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.feature-card p {
    color: #6b7280;
    line-height: 1.6;
}
</style>

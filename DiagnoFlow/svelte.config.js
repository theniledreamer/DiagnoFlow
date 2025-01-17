import adapter from '@sveltejs/adapter-vercel';

const config = {
  kit: {
    adapter: adapter({
      // options here are optional
      runtime: 'nodejs20.x' // Ensure this matches Vercel's supported Node.js runtime
    })
  }
};

export default config;

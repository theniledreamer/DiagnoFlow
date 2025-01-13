import vercel from '@sveltejs/adapter-vercel';

const config = {
  kit: {
    adapter: vercel({
      // options here are optional
      runtime: 'nodejs18.x' // Ensure this matches Vercel's supported Node.js runtime
    })
  }
};

export default config;

module.exports = {
  trailingSlash: true, // com ele é possível escolher se o site terá uma barra no final ou não

  async redirects() {
    // com essa função é possível facilmente criar redirecionamentos
    return [
      {
        source: "/perguntas",
        destination: "/faq",
        permanent: true,
      },
    ];
  },
};

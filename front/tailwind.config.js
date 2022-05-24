module.exports = {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
  corePlugins: {
    // AntDesignのスタイルを打ち消してしまうため、Preflightを無効にする
    preflight: false,
  },
};

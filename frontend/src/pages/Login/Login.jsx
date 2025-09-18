export default function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-[#fdf7f2] px-4">
      <div className="w-full max-w-md bg-white rounded-xl shadow-lg p-8">
        <h1 className="text-2xl font-bold text-[#3b2e2a] mb-6 text-center">
          Welcome Back
        </h1>

        <form className="space-y-4">
          <div>
            <label className="block text-gray-700 mb-1" htmlFor="email">
              Email
            </label>
            <input
              type="email"
              id="email"
              placeholder="you@example.com"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#6b4226]"
            />
          </div>

          <div>
            <label className="block text-gray-700 mb-1" htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              placeholder="********"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#6b4226]"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-[#6b4226] text-white py-3 rounded-lg font-semibold shadow-md hover:bg-[#5a3721] transition"
          >
            Log In
          </button>
        </form>

        <p className="mt-4 text-center text-gray-600 text-sm">
          Don't have an account?{" "}
          <a href="/signup" className="text-[#6b4226] font-semibold hover:underline">
            Sign Up
          </a>
        </p>
      </div>
    </div>
  );
}

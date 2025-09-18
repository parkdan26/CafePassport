export default function FrontPage() {
  return (
    <div className="font-serif bg-[#fdf7f2] text-[#3b2e2a] min-h-screen flex flex-col">
      <nav className="w-full max-w-6xl mx-auto flex justify-between items-center px-6 py-4">
        <h1 className="font-bold text-xl">Café Passport</h1>
        <div className="flex space-x-4">
          <button className="bg-[#6b4226] text-white px-4 py-2 rounded-md hover:bg-[#5a3721] transition">
            Log in
          </button>
          <button className="bg-[#6b4226] text-white px-4 py-2 rounded-md hover:bg-[#5a3721] transition">
            SignUp
          </button>
        </div>
      </nav>

<main className="flex-grow max-w-6xl w-full px-6 py-12 mx-auto grid items-center">
  <div className="space-y-3">
    <h2 className="text-3xl font-bold leading-snug">
      Discover cafés. Collect stamps. Earn rewards.
    </h2>
    <p className="text-lg text-gray-700">
      Join the café community and track your coffee adventures.
    </p>
    <button className="bg-[#6b4226] text-white px-6 py-3 rounded-lg font-semibold shadow-md hover:bg-[#5a3721] transition">
      Start Your Passport Today
    </button>
  </div>

  <div className="rounded-xl bg-gradient-to-br from-[#d7c4b2] to-[#b08b65] h-56 flex items-center justify-center text-xl font-semibold text-white shadow-md p-6 text-center">
    Discover cafés. Collect stamps.
    <br />
    Share with Friends.
  </div>
</main>
      <footer className="w-full max-w-6xl px-6 py-6 text-center text-gray-600 text-sm border-t mx-auto">
        &copy; 2025 Café Passport. All rights reserved.
      </footer>
    </div>
  );
}

let toastTimeout; // var kosong untuk simpan timer

function showToast(message, type = 'info', duration = 3000) {
  const toast = document.getElementById('toast-notification');
  const toastMessage = document.getElementById('toast-message');

  if (!toast || !toastMessage) return; // elemen tidak ditemukan

  clearTimeout(toastTimeout); // toast lama belum hilang, batalkan timer

  // set message
  toastMessage.textContent = message;

  // reset tampilan toast
  toast.className = 'fixed top-5 right-5 w-full max-w-xs p-4 rounded-lg shadow-lg z-[100] opacity-0 translate-x-full transition-all duration-300 ease-in-out';
  toastMessage.className = 'ms-3 text-sm font-normal flex-grow';

  // tipe toast
  if (type === 'success') {
    toast.classList.add('bg-white', 'text-[#4B40B5]', 'border', 'border-[#4B40B5]');
  } else if (type === 'error') {
    toast.classList.add('bg-red-50', 'text-red-800', 'border', 'border-red-200');
  } else { // info
    toast.classList.add('bg-white', 'text-gray-900', 'border', 'border-gray-200');
  }

  // show toast
  toast.classList.remove('opacity-0', 'translate-x-full'); // hapus class yang sembunyikan toast
  toast.classList.add('opacity-100', 'translate-x-0'); // tambahin class yang menampilkan toast

  // timer baru untuk sembunyiin
  toastTimeout = setTimeout(() => {
    hideToast();
  }, duration);
}

function hideToast() {
  const toast = document.getElementById('toast-notification');
  if (!toast) return;
  toast.classList.remove('opacity-100', 'translate-x-0');
  toast.classList.add('opacity-0', 'translate-x-full');
}
async function downloadJpgCard() {
    const card = document.getElementById('businessCard');

    const scale = 3;  
    const canvas = await html2canvas(card, {
        scale: scale,
        useCORS: true
    });

    const imgData = canvas.toDataURL('image/jpeg', 1.0); 

    const link = document.createElement('a');
    link.href = imgData;
    link.download = 'business-card.jpg';
    link.click();
}

async function downloadPdfCard() {
    const card = document.getElementById('businessCard');

    const scale = 3; 
    const canvas = await html2canvas(card, {
        scale: scale,
        useCORS: true
    });

    const imgData = canvas.toDataURL('image/jpeg', 1.0); 

    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF({
        orientation: 'landscape',
        unit: 'in',
        format: [3.5, 2]
    });

    pdf.addImage(imgData, 'JPEG', 0, 0, 3.5, 2);
    pdf.save('business-card.pdf');
}

async function downloadQrcode() {
    const card = document.getElementById('qr_code');

    const scale = 3;  
    const canvas = await html2canvas(card, {
        scale: scale,
        useCORS: true
    });

    const imgData = canvas.toDataURL('image/jpeg', 1.0); 

    const link = document.createElement('a');
    link.href = imgData;
    link.download = 'QR Code.jpg';
    link.click();
}

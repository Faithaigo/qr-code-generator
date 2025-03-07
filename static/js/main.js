
const card = document.getElementById('businessCard');
const code = document.getElementById('qr_code');


async function getCanvas(element){
    const scale = 3;  
    const canvas = await html2canvas(element, {
        scale: scale,
        useCORS: true
    });

    return canvas.toDataURL('image/jpeg', 1.0); 

}


async function downloadJpgCard() {
    const imgData = await getCanvas(card)
    const link = document.createElement('a');
    link.href = imgData;
    link.download = 'business-card.jpg';
    link.click();
}

async function downloadPdfCard() {
    const imgData = await getCanvas(card)

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
    const imgData = await getCanvas(code)
    
    const link = document.createElement('a');
    link.href = imgData;
    link.download = 'QR Code.jpg';
    link.click();
}

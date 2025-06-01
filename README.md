- ## Instalasi Template
```bash
git clone https://github.com/IshikawaUta/templates-portofolio-flask-1
```
```bash
cd templates-portofolio-flask-1
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements. txt
```
- ## Menjalankan Project di Lokal
- Buat file dengan nama `.env` dengan isi file:
```python
MAIL_SERVER=smtp.gmail.com ## default
MAIL_PORT=587 ## default
MAIL_USE_TLS=True ## default
MAIL_USE_SSL=False ## default
MAIL_USERNAME=alamatemail@anda.com
MAIL_PASSWORD=passwordemailanda
RECIPIENT_EMAIL=alamatemailanda.com
```
- Run project
```bash
flask --app app.py --debug run
```
- ## Mengoptimasi SEO dengan Domain Anda
- edit file `sitemap.xml` contoh:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <!-- ubah dengan alamat domain anda -->
      <loc>https://templates-ekasaputra-satu.vercel.app/</loc>
      <!-- ubah dengan alamat domain anda -->
      <!-- sesuaikan dengan tanggal terakhir kali anda mengupdate website anda -->
      <lastmod>2025-06-01</lastmod> <changefreq>monthly</changefreq> <priority>1.0</priority> </url>
      <!-- sesuaikan dengan tanggal terakhir kali anda mengupdate website anda -->
</urlset>
```
- edit file `robots.txt` ubah url sitemap pada baris terakhir file `robots.txt` contoh:
```python
Sitemap: https://templates-ekasaputra-satu.vercel.app/sitemap.xml
## ubah dengan alamat domain anda
```
- edit `script ld+json` pada file html
- sesuaikan domain, name, description, dll pada website anda contoh:
```html
    <script type="application/ld+json">
        [
          {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "Eka Saputra",
            "url": "https://templates-ekasaputra-satu.vercel.app",
            "image": "{{ url_for('static', filename='img/ft-sy.jpg') }}",
            "jobTitle": "Web Developer",
            "additionalType": "https://schema.org/SoftwareDeveloper",
            "description": "Jelajahi templates portofolio saya, kami menyediakan templates-templates portofolio keren, responsive dan modern, serta jasa pembuatan website.",
            "knowsAbout": [
              "Web Development", "Front-end Development", "Back-end Development",
              "HTML5", "CSS3", "JavaScript", "Python", "Flask", "Tailwind CSS",
              "Bootstrap", "React", "Gatsby", "Astro", "Responsive Design"
            ],
            "sameAs": [
              "https://github.com/IshikawaUta",
              "https://wa.me/+62895701060973"
            ],
            "contactPoint": {
              "@type": "ContactPoint",
              "contactType": "Sales or technical support",
              "email": "mailto:komikers09@gmail.com"
            }
          },
          {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Templates Portofolio Eka Saputra",
            "url": "https://templates-ekasaputra-satu.vercel.app",
            "description": "Jelajahi templates portofolio saya, kami menyediakan templates-templates portofolio keren, responsive dan modern, serta jasa pembuatan website.",
            "potentialAction": {
              "@type": "SearchAction",
              "target": {
                "@type": "EntryPoint",
                "urlTemplate": "https://templates-ekasaputra-satu.vercel.app/cari?q={search_term_string}"
              },
              "query-input": "required name=search_term_string"
            }
          }
        ]
    </script>
```
# peringantan file `.env` hanya digunakan untuk kebutuhan lokal jangan melakukan push ke github
# untuk kebutuhan deployment masukan semua isi file `.env` pada environment variables saat deploy di vercel

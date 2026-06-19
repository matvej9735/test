// Обработчик всех запросов
export default {
  async fetch(request) {
    // Получаем URL
    const url = new URL(request.url);
    
    // Приветствие
    if (url.pathname === "/" || url.pathname === "/hello") {
      return new Response("👋 Hello from Cloudflare Worker!", {
        headers: { "Content-Type": "text/plain" }
      });
    }
    
    // JSON ответ
    if (url.pathname === "/api") {
      return new Response(JSON.stringify({
        message: "Hello World!",
        time: new Date().toISOString(),
        status: "success"
      }), {
        headers: { "Content-Type": "application/json" }
      });
    }
    
    // Получить параметры из URL
    if (url.pathname === "/user") {
      const name = url.searchParams.get("name") || "Guest";
      return new Response(`Hello, ${name}!`, {
        headers: { "Content-Type": "text/plain" }
      });
    }
    
    // Отправить POST данные
    if (url.pathname === "/echo" && request.method === "POST") {
      const body = await request.json();
      return new Response(JSON.stringify({
        received: body,
        method: "POST"
      }), {
        headers: { "Content-Type": "application/json" }
      });
    }
    
    // 404 - не найдено
    return new Response("Page not found", { status: 404 });
  }
};

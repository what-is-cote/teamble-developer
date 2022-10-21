const BASE = "https://h6uc5l8b1g.execute-api.ap-northeast-2.amazonaws.com/dev";

export async function client(PATH, options) {
  const url = BASE + PATH;

  if (PATH.match(/\/+(cart)/g)) {
  } else if (PATH.match(/\/+(products)+\/[1-9]/g)) {
    return new Promise((r) => {
      setTimeout(() => {
        r({
          id: 1,
          imageUrl: null,
          price: 1000,
          name: "커피",
          productOptions: [
            {
              id: 1,
              stock: 0,
              name: "커피잔 100개번들",
              price: 2000,
            },
            {
              id: 2,
              stock: 10,
              name: "커피잔 1000개번들",
              price: 20000,
            },
          ],
        });
      }, 1000);
    });
  } else {
    return new Promise((r) => {
      setTimeout(() => {
        r([
          {
            id: 1,
            imageUrl: null,
            price: 1000,
            name: "커피",
          },
          {
            id: 2,
            imageUrl: null,
            price: 5000,
            name: "커피 홀더",
          },
        ]);
      }, 1000);
    });
  }

  // try {
  //   const res = await fetch(url, (options = {}));

  //   if (res.ok) {
  //     const data = await res.json();
  //     return data;
  //   }
  // } catch (err) {
  //   throw new Error(err);
  // }
}

function example() {
    // Clear the existing cart.
    CartJS.clear();
   
    // Add 3x "12345678" items, with a custom "size" property of "XL".
    CartJS.addItem(12345678, 3, {
      "size": "XL"
    });
   
    // Add multiple items in a single call. 
    CartJS.addItems([
      {
        id: 12345678,
        quantity: 3,
        properties: {
          "size": "XL"
        }
      },
      {
        id: 87654321,
        quantity: 2
      }
    ]);
   
    // Set a custom cart note.
    CartJS.setNote('This is a custom cart note.');
  }
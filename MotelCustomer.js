const customer = {
    firstName: 'Mike',
    lastName: 'Tyson',
    birthday: '1966-06-30',
    gender: 'Male',
    height: '1.78m',
    weight: '100kg',
    roomPreferences: ['Large Bed','Balcony','Room Service','Bathtub'],
    paymentMethod: 'Cash',
    address: {
        street: '123 Street',
        city: 'New York',
        state: 'New York',
        postalCode: 'ABC123',
        country: 'USA'
    },
    phoneNumber: '1-709-700-7000',
    dates: {
        checkIn: '2023-12-01',
        checkOut: '2023-12-31'
    },
    getAge: function() {
        const today = new Date();
        return today.getFullYear() - this.birthday.slice(0,4)
    },
    durationStay: function() {
        return this.dates.checkOut.slice(9,10) - this.dates.checkIn.slice(9,10)
    }
}

const customerDescribed = `Hello, I am ${customer.firstName} ${customer.lastName}. I was born on ${customer.birthday} and am currently ${customer.getAge()} years old.
I am currently staying in this awesome hotel with a ${customer.roomPreferences[0]} and a ${customer.roomPreferences[3]}. I will be staying here for ${customer.durationStay()} days.`
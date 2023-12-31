
function Auctionslist({products, isLoading}) {
    return (
        <div>
        {isLoading && 
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        }

      {products.length === 0 && !isLoading && <p>No products found</p>}


      <div className="container">
        {products.map(({ id, title, price, category, image}) => (
          <a href={`/product/${id}` } key={id}>
            <div className="card mb-3">
              <div className="row g-0">
                <div className="col-md-4">
                  <img src={image} className="img-fluid rounded-start" alt={title}></img>
                </div>
                <div className="col-md-8">
                  <div className="card-body">
                    <h5 className="card-title">{title}</h5>
                    <p className="card-text">{price}</p>
                    <p className="card-text"><small className="text-body-secondary">{category}</small></p>
                  </div>
                </div>
              </div>
            </div>
          </a>
        ))}
      </div>
      </div>
    )
}

export default Auctionslist;
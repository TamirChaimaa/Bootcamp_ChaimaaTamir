import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import ImageCard from '../components/ImageCard';
import './Search.css';

const Search = () => {
  const { query } = useParams();
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchImages = async () => {
      const response = await axios.get(`https://api.pexels.com/v1/search?query=${query}&per_page=30`, {
        headers: {
          Authorization: 'YOUR_PEXELS_API_KEY'
        }
      });
      setImages(response.data.photos);
    };
    fetchImages();
  }, [query]);

  return (
    <div className="gallery">
      {images.map(img => <ImageCard key={img.id} image={img} />)}
    </div>
  );
};

export default Search;
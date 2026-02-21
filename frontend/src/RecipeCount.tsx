import React from 'react';
import { useListRecipesRecipesGet } from './api/recipes';

const RecipeCount: React.FC = () => {
  const { data, isLoading, error } = useListRecipesRecipesGet();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading recipes.</div>;

  console.log('Recipe API response:', data);
  return <div>Recipe count: {Array.isArray(data) ? data.length : 0}<pre>{JSON.stringify(data, null, 2)}</pre></div>;
};

export default RecipeCount;
